from FacebookAPI import main
import nose

class test_main():


    @classmethod
    def setUpClass(cls):

        cls.userData = {"id": 0, "username": "shai", "firstName": "Shai", "lastName": "Edy", "email": "shai@gmail.com",
                    "password": "12345", "phone": "050-123-4567", "userStatus": 0, 'key': 'value'}

        cls.storeActions = main.PetStoreActions()

    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_createUser(self):
        #self.userData
        ref = self.storeActions.getUserByName("shai")
        assert (ref.text != u'')

    #def test_getUserByName:

    #def test_deleteUserByName:



if __name__ == '__main__':
    nose.run()
