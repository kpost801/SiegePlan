from flask import Blueprint, render_template, redirect, url_for, request, flash
from core.models import User
from core import db

auth = Blueprint("auth", __name__)


