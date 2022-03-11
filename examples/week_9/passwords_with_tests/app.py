from flask import Flask, render_template, request, jsonify
from functools import wraps
import mysql.connector
import bcrypt
import configparser
import io

import passwords

app = passwords.create_app()
