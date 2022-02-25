# Agora Cloud Recording on GCP

## About
An AGORA video call application with cloud recording feature for GCP.<br/>
This is a one-on-one call which involves a call invitation and acceptance. <br/>
You have the option to record the video call when it is in progress.

Only sqlite is supported. To use other databases, install the required drivers and update the `SQLALCHEMY_DATABASE_URI` environment variable with the corresponding details. Learn more from the  [Flask SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/#configuration-keys)<br/>

I created this to help users to follow some technical articles I'm yet to write. You can checkout out my other articles for now<br/>
1. [Dev.to](https://dev.to/mupati/build-a-scalable-video-chat-app-with-agora-in-flask-52pg)
2. [Medium](https://mupati.medium.com/build-a-scalable-video-chat-app-with-agora-in-flask-e8f4de554f25)

## Setup

1. Clone or download the repository
   ```bash
   git clone git@github.com:Mupati/agora-gcp-cloud-recording.git
   ```
2. Create your `.flaskenv` file and update your variables
   ```bash
   cd agora-gcp-cloud-recording
   cp .flaskenv.example .flaskenv
   ```
3. Install project dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize db and apply migrations
   ```bash
   flask db init
   flask db migrate -m "Create users table"
   flask db upgrade
   ```

5. Start application on development server
   ```bash
   flask run
   ```