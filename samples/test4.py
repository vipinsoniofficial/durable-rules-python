from durable.lang import *
from flask import Flask
from flask_restx import Api, Resource, fields
from durable.lang import ruleset, when_all, m, post, _main_host

app = Flask(__name__)
api = Api(app, version='1.0', title='Data API', description='A simple Data Storing API', )

ns = api.namespace('School Fee', description='CRUD operations')
school_fees_info = api.model('Fees', {'school': fields.String("School Name"),
                                      'location': fields.String("Location Name")})


class Work:
    fees = 0

    def get(self, data):
        try:
            with ruleset('test'):
                @when_all((m.school == 'GANDHI SCHOOL') & (m.location == 'JAIPUR'))
                def school_abc(c):
                    global fees
                    fees = 1000
                    print('fees:', fees)

            post('test', data)
            return 'fees: ' + str(fees), 201
        except Exception:
            raise Exception("Issue in finding user")

    def add(self, data):
        try:
            """ if _main_host._ruleset_directory is not None:
                _main_host._ruleset_directory.clear() """

            with ruleset('data'):
                @when_all((m.school == 'GANDHI SCHOOL') & (m.location == 'JAIPUR'))
                def school_abc(c):
                    global fees
                    fees = 1000

                @when_all((m.school == 'DDU SCHOOL') & (m.location == 'DELHI'))
                def school_abc(c):
                    global fees
                    fees = 2000

            post('data', data)

            return {'Fees': fees}, 201

        except Exception:
            raise Exception("Issue in adding user")


work = Work()


@ns.route('/')
class FeeCheck2(Resource):
    @ns.expect(school_fees_info)
    def post(self):
        return work.get(api.payload)


@ns.route('/s')
class FeeCheck1(Resource):
    @ns.expect(school_fees_info)
    def post(self):
        data = api.payload
        return work.add(data)


if __name__ == '__main__':
    app.run(port=9999, debug=True)
