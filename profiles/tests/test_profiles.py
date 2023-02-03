from django.urls import reverse
from django.contrib.auth.models import User
import pytest

from profiles.models import Profile


@pytest.mark.django_db
class TestProfile:

    def test_index(self, client):

        user_sam = User.objects.create_user(username='Sam', password='test01234')
        user_marcel = User.objects.create_user(username='Marcel', password='test01234')

        Profile.objects.create(user=user_sam, favorite_city='Paris')
        Profile.objects.create(user=user_marcel, favorite_city='Pragues')

        # --
        response = client.get(reverse('profiles_index'))
        html = response.content.decode()

        assert response.status_code == 200
        assert 'Profiles' in html
        assert 'Sam' in html
        assert 'Marcel' in html

    def test_profile(self, client):

        user_sam = User.objects.create_user(username='Sam',
                                            password='test01234',
                                            first_name='Samuel',
                                            last_name='Pignon',
                                            email='sam@mail.com')

        Profile.objects.create(user=user_sam, favorite_city='Paris')

        # --
        response = client.get(reverse('profile', args=[user_sam.username]))
        html = response.content.decode()

        assert response.status_code == 200
        assert 'Sam' in html
        assert 'First name: Samuel' in html
        assert 'Last name: Pignon' in html
        assert 'Email: sam@mail.com' in html
        assert 'Favorite city: Paris' in html
