from durable.lang import statechart, state, when_all, to, m, post, assert_fact
from flask_restx import Api, fields, Resource
from flask import Flask


app = Flask(__name__)
api = Api(app, version='1.0', title='Data API', description='A simple Data Storing API', )

lw = api.namespace('Fee by location', description='CRUD operations')
location_wise_info = api.model('location_wise', {'location': fields.String("Location Name")})

with statechart('data'):
    with state('info'):
        with state('PILANI'):
            @to('process')
            @when_all(m.location == 'PILANI')
            def pilani_schools(c):
                global fees
                fees = {"BIRLA SCHOOL": 30000,
                        "GOYAL SCHOOL": 22000,
                        "RK ACADEMY": 24000
                        }
                print(fees)


@lw.route('/')
class LocationWise(Resource):
    @lw.expect(location_wise_info)
    def post(self):
        assert_fact('data', api.payload)
        return 'fees: ' + str(fees)


if __name__ == '__main__':
    app.run(port=9990, debug=True)