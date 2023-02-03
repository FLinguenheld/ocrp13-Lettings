from django.urls import reverse


class TestHome:

    def test_connection(self, client):

        response = client.get(reverse('index'))

        assert response.status_code == 200
        assert 'Welcome to Holiday Homes' in response.content.decode()
