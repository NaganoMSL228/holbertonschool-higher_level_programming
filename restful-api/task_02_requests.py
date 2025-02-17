#!/usr/bin/python3
''' Module that fetches data from an API '''

import requests
import csv


def fetch_and_print_posts():
    '''Fetches data from an API and prints post titles'''
    url = 'https://jsonplaceholder.typicode.com/posts'
    try:
        response = requests.get(url)
        response.raise_for_status()
