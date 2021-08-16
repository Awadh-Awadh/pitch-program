from . import main
from flask import render_template, url_for
from .forms import PitchForm
from ..models import Pitch

@main.route('/')
def index():
  return render_template('index.html')


@main.route('/pitches')
def pitches():
  upvote = 2
  downvote = 1
  pitches = [
    {
      "pitch": "I recently launched a website for people who like to work on classic cars.      The website has articles and videos with tutorials on how to work on cars",
      "name" : "John Doe"

    },
    {
      "pitch" : "I am in the planning stages of a mobile app company in New York. The company will create mobile apps which will help people write business plans on their mobile devices.",
      "name" : "Mchimba kisima"
    }

  ]

  pitch_form = PitchForm()
  add_pitch = Pitch(pitch=pitch_form.pitch.data, name = pitch_form.name.data,)


  return render_template('pitches.html', pitch = pitches)
