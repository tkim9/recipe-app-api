from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'tongminkim9@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        
        # Check email
        self.assertEqual(user.email, email)
        
        # check password
        # password is encrypted so need to use .check_password helper function from django
        # returns True or False
        self.assertTrue(user.check_password(password))
        
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')
        
        self.assertEqual(user.email, email.lower())
        
    def test_new_user_invalid_email(self):
        """
        Test creating user with no email raises error
        """
        # asserRaises(ValueError) will raise an error if ValueError is not raised
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
            
            
    
    def test_create_new_superuser(self):
        """
        Test creating a new superuser
        """
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)