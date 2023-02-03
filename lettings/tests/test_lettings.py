from django.urls import reverse
import pytest

from lettings.models import Letting
from lettings.models import Address


@pytest.mark.django_db
class TestLettings:

    def test_index(self, client):

        address_0 = Address.objects.create(number=1,
                                           street='Backerstreet',
                                           city='London',
                                           state=10,
                                           zip_code=20,
                                           country_iso_code='UK')

        Letting.objects.create(title='Sherlock House',
                               address=address_0)

        # --
        response = client.get(reverse('lettings_index'))
        html = response.content.decode()

        assert response.status_code == 200
        assert 'Lettings' in html
        assert 'Sherlock House' in html

    def test_letting(self, client):

        address_0 = Address.objects.create(number=1,
                                           street='Backerstreet',
                                           city='London',
                                           state=10,
                                           zip_code=20,
                                           country_iso_code='UK')

        letting_0 = Letting.objects.create(title='Sherlock House',
                                           address=address_0)

        # --
        response = client.get(reverse('letting', args=[letting_0.pk]))
        html = response.content.decode()

        assert response.status_code == 200
        assert 'Sherlock House' in html
        assert '1 Backerstreet' in html
        assert 'London' in html
        assert 'UK' in html
