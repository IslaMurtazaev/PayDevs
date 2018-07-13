from django.shortcuts import render
from project.serializers import ProjectSerializer, ProjectListSerializer
from PayDevs.decorators import serialize_exception
from account.models import UserORM


class CreateProjectView(object):
	def __init__(self, create_project_interactor):
		self.create_project_interactor=create_project_interactor

	@serialize_exception
	def post(self, *args, **kwargs):
		title = kwargs.get('title')
		description = kwargs.get('description')
		user = UserORM.objects.get(id=kwargs.get('user_id'))
		type_of_payment = kwargs.get('type_of_payment')
		project = self.create_project_interactor.set_params(title=title, description=description, user=user, type_of_payment=type_of_payment).execute()
		body = ProjectSerializer.serializer(project)
		status = 201
		return body, status
		


class ProjectView(object):
	def __init__(self, get_project_interactor):
		self.get_project_interactor=get_project_interactor

	@serialize_exception
	def get(self, *args, **kwargs):
		title = kwargs.get('title')
		project = self.get_project_interactor.set_params(title=title).execute()
		body = ProjectSerializer.serializer(project)
		status = 200
		return body, status


class ProjectAllView(object):
	def __init__(self, get_project_interactor):
		self.get_project_interactor=get_project_interactor

	@serialize_exception
	def get(self, title):
		projects = self.get_project_interactor.set_params(title=title).execute()
		body = ProjectListSerializer.serializer(projects)
		status = 200
		return body, status