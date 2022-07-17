import os

from flask import Blueprint, redirect, request
import tweepy

from weather_name.models import User

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

blueprint = Blueprint("public", __name__)


@blueprint.route("/", methods=["GET"])
def index():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET, request.host_url)
    redirect_url = "https://twitter.com"
    oauth_token = request.args.get("oauth_token")
    oauth_verifier = request.args.get("oauth_verifier")
    if oauth_token and oauth_verifier:
        # oauth_token
        try:
            auth.request_token = {
                "oauth_token": oauth_token,
                "oauth_token_secret": oauth_verifier,
            }
            auth.get_access_token(oauth_verifier)
            api = tweepy.API(auth)
            # User作成
            # Error
            tw_user = api.me()
            user = User.query.filter_by(user_id=tw_user.id).first()
            if user:
                user.update(
                    token=auth.access_token,
                    token_secret=auth.access_token_secret,
                )
            else:
                User.create(
                    user_id=tw_user.id,
                    token=auth.access_token,
                    token_secret=auth.access_token_secret,
                )

        except tweepy.TweepError:
            print("Request token missing")
    else:
        try:
            redirect_url = auth.get_authorization_url()
        except tweepy.TweepError as e:
            print(e)
    print("redirect_url", redirect_url)
    return redirect(redirect_url)
