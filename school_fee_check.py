from durable.lang import ruleset, when_all, m, post, assert_fact, when_any, pri
from flask import Flask
from flask_restx import Api, fields, Resource

app = Flask(__name__)
api = Api(app, version='1.0', title='Data API', description='A simple Data Storing API', )

ns = api.namespace('School Fee', description='CRUD operations')
school_fees_info = api.model('Fees', {'school': fields.String("School Name"),
                                      'location': fields.String("Location Name")})

locations = ['DELHI', 'JAIPUR', 'PUNE', 'PILANI']
fees = 0

with ruleset('data'):
    @when_all((m.school == "GANDHI SCHOOL") & (m.location == "JAIPUR"))
    def fee_info(c):
        global fees
        fees = 25000
        print('fees:', fees)


    @when_all((m.school == 'DDU SCHOOL') & (m.location == 'DELHI'))
    def fee_info(c):
        global fees
        fees = 28000
        print('fees:', fees)


    @when_all((m.school == 'BIRLA SCHOOL') & (m.location == 'PILANI'))
    def fee_info(c):
        global fees
        fees = 30000
        print('fees:', fees)


    @when_all((m.school == 'MH SCHOOL') & (m.location == 'PUNE'))
    def fee_info(c):
        global fees
        fees = 26000
        print('fees:', fees)


    @when_all((m.school == "SCHOOL") & (m.location == "PAN"))
    def fee_info(c):
        global fees
        fees = {"BIRLA SCHOOL, PILANI": 30000,
                "GANDHI SCHOOL, JAIPUR": 25000,
                "DDU SCHOOL, DELHI": 28000,
                "MH SCHOOL, PUNE": 26000
                }
        print(fees)


    @when_any(pri(1), (m.school.matches(".*[A-Za-z0-9].*")) | (m.location.matches("[a-z]")))
    def fee_info(c):
        global fees
        fees = 'Enter proper school name'
        print(fees)

    @when_any(pri(2), m.loaction.matches('.*[A-Za-z0-9].*') | (m.school.matches(".* SCHOOL.*")))
    def fee_info(c):
        global fees
        fees = 'Enter proper location name'
        print(fees)


@ns.route('/')
class FeeCheck(Resource):
    @ns.expect(school_fees_info)
    def post(self):
        try:
            school_data = api.payload
            print(school_data)
            post('data', api.payload)
            return 'fees: ' + str(fees)
        except Exception:
           raise Exception('Exception in finding fee')


@ns.route('/fee')
class FeeChecking(Resource):
    @ns.expect(school_fees_info)
    def post(self):
        try:
            school_data = api.payload
            assert_fact('data', school_data)
            return 'fees: ' + str(fees)
        except Exception:
            raise Exception('Exception in finding fee')


if __name__ == '__main__':
    app.run(port=9999, debug=True)
