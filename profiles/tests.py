import pytest

from django.core.management import call_command

@pytest.fixture(scope='session')
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'profile_data.json')

@pytest.mark.django_db
def test_index_profiles_get(client):
    response = client.get('/profiles/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_profiles_get(client):
    response = client.get('/profiles/HeadlinesGazer/')
    assert b"HeadlinesGazer" in response.content
    assert response.status_code == 200
