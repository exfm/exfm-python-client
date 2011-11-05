exfm-python-client
====================

A simple client library to remotely access the `exfm REST API` as per [http://ex.fm/api](http://ex.fm/api).

# Installation

    $ pip install -e git+https://github.com/exfm/exfm-python-client.git#egg=exfm-python-client

# Usage

## Setup

    >>> from exfm import ExfmClient
    >>> exfm = ExfmClient()

All interactions with the exfm API are through methods of an instance of ExfmClient.

## Getting data

### Get a user's profile information by username

    >>> jm = exfm.get_user('jm')
    >>> from pprint import pprint  # For pretty printing of returned data, just for this tutorial.
    >>> pprint(jm)
    {'status_code': 200,
     'status_text': 'OK',
     'user': {'background': {'color': '#FFFFFF',
                             'image': 'http://24.media.tumblr.com/tumblr_lp2mpfODpc1qazdhko1_500.gif',
                             'is_default': False,
                             'position': 'left top',
                             'repeat': 'repeat',
                             'use_image': True},
              'bio': 'Software developer at exfm, composer, tabla player.',
              'image': {'medium': 'http://images.extension.fm/avatar_medium_jm',
                        'original': 'http://images.extension.fm/avatar_orig_jm',
                        'small': 'http://images.extension.fm/avatar_small_jm'},
              'import_feeds': [{'name': "jm's tumblr",
                                'type': 'tumblr',
                                'url': 'http://nikhilbanerjee.tumblr.com/api/read/json?type=audio&debug=1'},
                               {'name': "jm's tumblr",
                                'type': 'tumblr',
                                'url': 'http://nikhilbanerjee.tumblr.com/api/read/json?type=audio&debug=1'}],
              'is_beta_tester': True,
              'location': 'New York, NY',
              'name': 'Jonathan Marmor',
              'total_followers': 54,
              'total_following': 97,
              'total_loved': 682,
              'username': 'jm',
              'viewer_following': False,
              'website': 'http://ex.fm'}}

All methods return a dictionary with the following top-level keys:

* status_code:  The HTTP status code of the response.  Anything other than 200 raises ExfmError.
* status_text:  Always 'OK' for successful responses.
* user, users, song, songs, etc:  The payload of the response, containing a dictionary representation of the object requested or a list of such objects.

The user profile object has some basic information about the user's profile page:

* background:  Images, colors, and positioning of profile page background.
* bio:  User-created biography.
* image:  User-uploaded avatar.
* import_feeds:  Automatically love songs that get posted on these sites.  Currently restricted to connected Tumblr accounts.
* is_beta_tester:  Flag if the user has permission to log in to exfm's next-generation awesomeness.
* name:  The user's real name, as entered by the user.
* total_followers:  The number of exfm users who are following this user.
* total_following:  The number of exfm users this user is following.
* username:  The user's exfm username.
* viewer_following:  Flag the current viewer following this user.  Not relevant for this client because there is no concept of a viewer.
* website:  The user's website, as entered by the user.

### Get a list of a user's loved songs

    >>> jm_loved = exfm.get_user_loved('jm')
    {'results': 20,
     'songs': [{'album': 'Good As I Been To You',
                'aliases': [],
                'artist': 'Bob Dylan',
                'buy_link': None,
                'id': '20szn',
                'image': {'large': 'http://userserve-ak.last.fm/serve/252/6690423.jpg',
                          'medium': 'http://userserve-ak.last.fm/serve/126/6690423.jpg',
                          'small': 'http://userserve-ak.last.fm/serve/64/6690423.jpg'},
                'last_loved': 'Fri Nov 04 23:10:42 +0000 2011',
                'listened': None,
                'loved_count': 1,
                'metadata_state': 'complete',
                'recent_loves': [],
                'similar_artists': ['bob dylan and the band',
                                    'neil young',
                                    'woody guthrie',
                                    'the band',
                                    'van morrison & bob dylan'],
                'sources': ['http://lolitainslacks.tumblr.com/post/3570403182',
                            'None'],
                'tags': ['folk rock',
                         'rock',
                         'singer-songwriter',
                         'folk',
                         'classic rock'],
                'title': 'Jim Jones',
                'trending_rank_today': 1782,
                'url': 'http://www.tumblr.com/audio_file/3570403182/tumblr_lhcmiouLWH1qzyrxg?plead=please-dont-download-this-or-our-lawyers-wont-let-us-host-audio',
                'user_love': {'client_id': 'exfm_api',
                              'comment': '',
                              'context': 'None',
                              'created_on': 'Fri Nov 04 23:10:42 +0000 2011',
                              'source': 'None',
                              'username': 'jm'},
                'viewer_love': None},
         {...}
     ],
     'start': 0,
     'status_code': 200,
     'status_text': 'OK',
     'total': 682}

Paginated responses have these additional keys:

* start:  The index of the first record returned.
* results:  The number of records returned in this response.
* total:  The total number of records available to this method.

Song objects in exfm are really Song-URL objects -- each is a record for a specific URL of an mp3 on the web.  For example, the first one returned by the call above is the song found at the URL:

    http://www.tumblr.com/audio_file/3570403182/tumblr_lhcmiouLWH1qzyrxg?plead=please-dont-download-this-or-our-lawyers-wont-let-us-host-audio

which is an mp3 that was uploaded as part of this Tumblr blog post:

    http://lolitainslacks.tumblr.com/post/3570403182

Exfm song objects have the following keys:

* title:  The title of this song.
* artist:  Artist name.
* album:  Album name.
* buy_link:  URL where you can and should buy the song.
* id:  Exfm's ID for this song object.  Use this to retrieve this exact record later.
* image:  URLs of small, medium, and large images for the album this song is on.
* last_loved:  Timestamp of the last time an exfm user loved this song.
* listened:  Timestamp of the last time an exfm user listened to this song.
* loved_count:  Number of exfm users who have loved this song.
* recent_loves:  Details of recent love events.  Steamy.
* similar_artists:  List of artists that might be similar to the artist associated with this song.
* sources:  URLs of the context in which this song was found.
* tags:  List of keyword tags that might be descriptive of this song.
* trending_rank_today:  Exfm's rank of how popular this song is on exfm today.
* url:  The URL of the file.
* user_love:  Details of the event when this user loved this song.

### Get a list of a user's followers and users the user is following

    >>> jm_followers = exfm.get_user_followers('jm')
    >>> jm_following = exfm.get_user_following('jm', start=12, results=3)
    >>> jm_following_ids = get_user_following_ids('jm')

Methods with paginated responses accept start and results arguments to specify which records are returned.  In the example above, jm_followers got the default records 0 through 19, jm_following got records 12, 13, and 14, and jm_following_ids got all the ids becuase that method is not paginated.  See [http://ex.fm/api](http://ex.fm/api) for a list of paginated and not paginated methods.

### Get time-based feed of events related to a user

See [http://ex.fm/api](http://ex.fm/api) for details of what each of these returns.

    >>> exfm.get_user_feed_love('jm')
    >>> exfm.get_user_activity('jm')
    >>> exfm.get_user_activity_with_verb('jm' 'love')
    >>> exfm.get_user_notifications('jm')


