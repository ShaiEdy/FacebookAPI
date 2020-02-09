from FacebookAPI import main
import nose


class test_main():

    @classmethod
    def setUpClass(cls):
        cls.userData = {"id": 0, "username": "shai", "firstName": "Shai", "lastName": "Edy", "email": "shai@gmail.com",
                        "password": "12345", "phone": "050-123-4567", "userStatus": 0, 'key': 'value'}

        cls.storeActions = main.PetStoreActions()

        cls.userDataAsString = '{"id":0,"username":"shai","firstName":"Shai","lastName":"Edy","email":"shai@gmail.com","password":"12345","phone":"050-123-4567","userStatus":0}'

    def setup(self):
        pass

    def teardown(self):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def test_createUser(self):
        ref = self.storeActions.getUserByName("shai")
        assert ref.ok == False

        self.storeActions.createUser(self.userData)

        ref = self.storeActions.getUserByName("shai")
        assert ref.ok == True

        self.storeActions.deleteUserByName("shai")

    def test_getUserByName(self):
        ref = self.storeActions.getUserByName("shai")
        assert ref.ok == False

        self.storeActions.createUser(self.userData)

        ref = self.storeActions.getUserByName("shai")
        assert ref.ok == True
        assert ref.text == self.userDataAsString

        self.storeActions.deleteUserByName("shai")

    def test_deleteUserByName(self):
        ref = self.storeActions.deleteUserByName("shai")
        assert ref.ok == False

        self.storeActions.createUser(self.userData)

        ref = self.storeActions.deleteUserByName("shai")
        assert ref.ok == True


if __name__ == '__main__':
    nose.run()
