from unittest import TestCase
from blog.models import Appointment
from .models import User



class AppointmentTest(TestCase):

    def setUp(self):
        # Creating a user type object
        self.user = User.objects.all()
      
    

    # Function to test if the appointment model is created
    def test_content(self):
        # Creating an appointment type object
        appointment = Appointment.objects.create(appointment_id='1234',
                                                      patient_id='234',
                                                      doctor_id='154',
                                                      appointment_date='2021-09-01')

                                                    
        
        expected_object_appointment_id = appointment.appointment_id # Expected department name
        expected_object_patient_id = appointment.patient_id # Expected date
        expected_object_doctor_id= appointment.doctor_id # Expected time
        expected_object_appointment_date = appointment.appointment_date # Expected is_accepted value
       

        self.assertEquals(expected_object_appointment_id, '1234') # Testing if the department name is correct
        self.assertEquals(expected_object_patient_id, '234') # Testing if the date is correct
        self.assertEquals(expected_object_doctor_id, '154') # Testing if the time is correct
        #self.assertFalse(expected_object_appointment_date, '2021-09-01') # Testing if the is_accepted value is correct
    

    # Function to delete the previously crested user
    def tearDown(self):
        self.user.delete()