from django.test import SimpleTestCase

# Create your tests here.

class TestFontTimes(SimpleTestCase):
    def test_(self):
        response = self.client.get("/font-times?word=Cho&repeat=2")
        self.assertContains(response, 'ChoCho')

    def test_1(self):
        response = self.client.get("/font-times?word=Cho&repeat=3")
        self.assertContains(response, 'ChoChoCho')

    def test_2(self):
        response = self.client.get("/font-times?word=Abc&repeat=3")
        self.assertContains(response, 'AbcAbcAbc')

class TestNoTeenSum(SimpleTestCase):
    def test_(self):
        response = self.client.get("/no-teen-sum?a=1&b=2&c=3")
        self.assertContains(response, 6)

    def test_1(self):
        response = self.client.get("/no-teen-sum?a=2&b=13&c=1")
        self.assertContains(response, 3)

    def test_2(self):
        response = self.client.get("/no-teen-sum?a=2&b=1&c=14")
        self.assertContains(response, 3)

class TestXYZThere(SimpleTestCase):
    def test_(self):
        response = self.client.get("/xyz-there?xyz=abcxyz")
        self.assertContains(response, True)

    def test_1(self):
        response = self.client.get("/xyz-there?xyz=abc.xyz")
        self.assertContains(response, False)

    def test_2(self):
        response = self.client.get("/xyz-there?xyz=xyz.abc")
        self.assertContains(response, True)
    
class TestCenteredAverage(SimpleTestCase):
    def test_(self):
        response = self.client.get("/centered-average?c=1&e=2&n=3&t=4&er=100&r=2&ed=5")
        self.assertContains(response, 3)
    def test_1(self):
        response = self.client.get("/centered-average?c=1&e=1&n=5&t=5&er=10&r=8&ed=7")
        self.assertContains(response, 5)
    def test_2(self):
        response = self.client.get("/centered-average?c=-10&e=-4&n=-2&t=-4&er=-2&r=0&ed=0")
        self.assertContains(response, -2)


