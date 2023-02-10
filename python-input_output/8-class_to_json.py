
#!/usr/bin/python3
"""8-class_to_json.py"""


def class_to_json(obj):
	"""class_to_json

	Args:
		obj (_type_): ll attributes of the obj Class are serializable:
    list, dictionary, string, integer and boolean

	Returns:
		_type_: _description_
	"""
	obj_dict = obj.__dict__
	aareturn (obj_dict)
