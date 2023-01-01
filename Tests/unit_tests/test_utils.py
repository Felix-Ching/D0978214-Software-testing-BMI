"""
This file demonstrates writing tests using the unittest module.
"""

import django
from django.test import TestCase
import os
import sys

"""
When we use Django, we have to tell it which settings we are using. We do this by using an environment variable, DJANGO_SETTINGS_MODULE. 
This is set in manage.py. We need to explicitly set it for tests to work with pytest.
"""

sys.path.append(os.path.join(os.getcwd(), 'Application'))
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "python_webapp_django.settings"
)
django.setup()

from app.utils import bmi_calculator

class BmiCalculatorTest(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS
        @classmethod
        def setUpClass(cls):
            super(BmiCalculatorTest, cls).setUpClass()

    def test_bmi_result_normal(self):
        """Tests bmi result."""
        height = 1.6
        weight = 55
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 21.48)
        self.assertEqual(bmi_means, '健康體位')

    def test_bmi_result_too_light(self):
        height = 1.7
        weight = 50
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 17.30)
        self.assertEqual(bmi_means, '過輕')

    def test_bmi_result_too_heavy(self):
        height = 1.6
        weight = 65
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 25.39)
        self.assertEqual(bmi_means, '過重')

    def test_bmi_result_little_fat(self):
        height = 1.6
        weight = 70
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 27.34)
        self.assertEqual(bmi_means, '輕度肥胖')

    def test_bmi_result_medium_fat(self):
        height = 1.6
        weight = 80
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 31.25)
        self.assertEqual(bmi_means, '中度肥胖')

    def test_bmi_result_too_heavy(self):
        height = 1.7
        weight = 120
        bmi, bmi_means = bmi_calculator(height, weight)
        self.assertEqual(bmi, 41.52)
        self.assertEqual(bmi_means, '重度肥胖')
