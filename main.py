from project import create_app
from flask import Flask, render_template, url_for, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = create_app()



if __name__ == "__main__":
    app.run(debug=True)