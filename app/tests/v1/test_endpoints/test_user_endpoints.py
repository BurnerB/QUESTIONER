import json
from app import create_app

from app.tests.v1.base_test import TestBaseTest as BaseTest

class TestUserEndpoints(BaseTest):

    def post_data_signup(self,data,path="/api/v1/user/auth/signup"):
        return self.client.post(path,data=json.dumps(data),headers={},content_type="application/json")

    def post_data_login(self,data,path="/api/v1/user/auth/signin"):
        return self.client.post(path,data=json.dumps(data),headers={},content_type="application/json")

    def test_good_sign_up(self):
        user ={
	         "firstname":"John",
	         "lastname":"Doe",
	         "email":"Johndoe@gmail.com",
	         "phone_number":"0729800000",
	         "username":"johny",
	         "password":"baba1234",
	         "confirmpassword":"baba1234"
             }

        """test good user signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code,201)

    def test_empty_first_name(self):
        user ={
	         "firstname":"",
	         "lastname":"Doe",
	         "email":"johndoe@gmail.com",
	         "phone_number":"0727988632",
	         "username":"johny",
	         "password":"baba123",
	         "confirmpassword":"baba123"
}
        """test empty firstname signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code,400)

    def test_empty_last_name(self):
        user ={
	         "firstname":"John",
	         "lastname":"",
	         "email":"johndoe@gmail.com",
	         "phone_number":"0727988632",
	         "username":"johny",
	         "password":"baba123",
	         "confirmpassword":"baba123"
}
        """test empty lastname signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code, 400)

        
    
    def test_empty_email_signup(self):
        user= {
                "firstname":"John",
                "lastname":"Doe",
                "email":"",
                "phone_number":"12345667",
                "username":"johny",
                "password":"baba123",
                "confirmpassword":"baba123"
            }
        """test empty email signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code, 400)

    def test_empty_phone_number_signup(self):
        user= {
                "firstname":"John",
                "lastname":"Doe",
                "email":"johndoe@gmail.com",
                "phone_number":"",
                "username":"johny",
                "password":"baba123",
                "confirmpassword":"baba123"
            }
        """test empty phone number signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code, 400)



    def test_empty_username_sign_up(self):
        user ={
                "firstname":"John",
                "lastname":"Doe",
                "email":"johndoe@gmail.com",
                "phone_number":"12345667",
                "username":"",
                "password":"baba123",
                "confirmpassword":"baba123"
            }
        """test empty username signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code, 400)
    
    def test_empty_password_sign_up(self):
        user ={
	         "firstname":"John",
	         "lastname":"Doe",
	         "email":"johndoe@gmail.com",
	         "phone_number":"0727988632",
	         "username":"johny",
	         "password":"",
	         "confirmpassword":"baba123"
}
        """test empty password signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code, 400)
    
    def test_empty_confirm_password_sign_up(self):
        user ={
	         "firstname":"John",
	         "lastname":"Doe",
	         "email":"johndoe@gmail.com",
	         "phone_number":"0727988632",
	         "username":"johny",
	         "password":"baba123",
	         "confirmpassword":""
}
        """test empty confirm password signup """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code,400)

    def test_confirm_password_not_match(self):
        user ={
	         "firstname":"John",
	         "lastname":"Doe",
	         "email":"johndoe@gmail.com",
	         "phone_number":"0727988632",
	         "username":"johny",
	         "password":"baba123",
	         "confirmpassword":"baba124"
}
        """test confirm password not match password  """
        response = self.post_data_signup(user)
        self.assertEqual(response.status_code,400)

    def test_good_signin(self):
        """test good signin """
        response = self.post_data_login(self.login)
        self.assertEqual(response.status_code, 200)



    def test_empty_username_log_in(self):
        user ={

                "username":"",
                "password":"baba123",
            }
        """test empty username signup """
        response = self.post_data_login(user)
        self.assertEqual(response.status_code, 400)

    def test_empty_password_login(self):
        user= {
                "username":"johny",
                "password":"",
            }
        """test empty email on signup """
        response = self.post_data_login(user)
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()