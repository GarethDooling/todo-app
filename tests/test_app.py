from flask_testing import TestCase
from application import app, db
from application.models import Tasks
from flask import url_for

class TestBase(TestCase):

    def create_app(self):
        # Defines the flask object's configuration for the unit tests
        app.config.update(
            DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        # Will be called before every test
        db.create_all()

        task1 = Tasks(name="new task", description= "this new task")

        db.session.add(task1)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.drop_all()

class TestCRUD(TestBase):

    def test_read_tasks(self):
        response = self.client.get(url_for('read'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('new task', str(response.data))
        self.assertIn('this new task', str(response.data))

    def test_create_tasks(self):
        response = self.client.post(
            url_for('create'),
            data=dict(name="created task", description="this is a create task"),
            follow_redirects=True
        )
        created_task = Tasks.query.get(2)
        self.assertEqual(created_task.name, "created task")
        self.assertIn('created task', str(response.data))
        self.assertIn('this is a create task', str(response.data))

    def test_update_tasks(self):
        response = self.client.post(
            url_for('update_task', id=1),
            data={"description": "Testing update functionality"},
            follow_redirects=True
        )
        self.assertIn("updated task", str(response.data))
        self.assertIn("this is an updated task", str(response.data))

    def test_delete_tasks(self):
        response = self.client.post(
            url_for('delete', name="new task"),
            follow_redirects=True
        )
        self.assertNotIn("new task", str(response.data))
