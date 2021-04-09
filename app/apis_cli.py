import click
import requests
from decouple import config
import re


BASE_URL = 'https://services.odata.org'

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


@click.group()
def apis():
    """A CLI wrapper for the API of Public APIs."""


@click.option('-id', '--value', prompt=True, help='Return search from this id')
@apis.command()
def search(value: str):
    """List all search entities"""
    response = requests.get(url=f"{BASE_URL}/TripPinRESTierService/People('{value}')")
    if response.status_code is 200:
        print(response.json())
    else:
        print(f'Could not get the APIs: {response.text}')


def check_email(ctx, param, value):
    values = value.split(",")
    for email in values:
        if (re.search(regex, email)):
            pass
        else:
            raise click.BadParameter('Invalid email')
    return values


@click.option('-region', '--region', prompt=True, default="", help='Provide region or optional')
@click.option('-country', '--country', prompt=True, default="", help='Provide country name or optional')
@click.option('-city_name', '--city_name', prompt=True, default="", help='Provide city name or optional')
@click.option('-address', '--address', prompt=True, default="", help='Provide address or optional')
@click.option('-email', '--email', callback=check_email, prompt=True, default="", help='Provide valid email or optional')
@click.option('-lastname', '--lastname', prompt=True, default="", help='Provide last name or optional')
@click.option('-firstname', '--firstname', required=True, prompt=True, help='Provide first name')
@click.option('-username', '--username', required=True, prompt=True, help='Provide username')
@apis.command()
def create_entity(username: str, firstname: str, lastname: str, email, address: str, city_name: str,
                  country: str, region: str):
    """Create new entities"""
    data_obj = {
        "UserName": username,
        "FirstName": firstname,
        "LastName": lastname,
        "Emails": email,
        "AddressInfo": [{"Address": address,
                         "City": {"Name": city_name, "CountryRegion": country, "Region": region}}]
    }
    headers = {'Content-type': 'application/json'}
    response = requests.post(url=f"{BASE_URL}/TripPinRESTierService/{config('KEY', None)}/People", headers=headers,
                             json=data_obj)
    if response.status_code is 201:
        print(response.json())
    else:
        print(f'Could not create entity: {response.text}')


choose_filter = ["UserName", "FirstName", "LastName", "MiddleName", "Gender", "Age"]


@click.option('-value', '--value', required=True, prompt=True, help='Provide filter to fetch user')
@click.option('-value_type', '--value_type', required=True, prompt=True, type=click.Choice(choose_filter, case_sensitive=True))
@apis.command()
def filter_user(value_type: str, value: str):
    """List all Filter users (entities)"""
    url = f"{BASE_URL}/TripPinRESTierService/People?$filter= {value_type} eq '{value}'"
    response = requests.get(url=url)
    if response.status_code is 200:
        print(response.json())
    else:
        print(f'Could not get the APIs: {response.text}')


if __name__ == '__main__':
    apis(prog_name='apis')