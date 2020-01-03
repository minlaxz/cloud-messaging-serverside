from firebase_admin import credentials , initialize_app

cred = credentials.Certificate('firebase/serviceKey.json')

try:
	initialize_app(cred, {
		'databaseURL' : 'https://laxz-test.firebaseio.com/',
		'databaseAuthVariableOverride': {
		'uid': 'laxz-writer'
		}
	})
except Exception as e:
	print(e)
