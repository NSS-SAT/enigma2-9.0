from Components.MenuList import MenuList
from Tools.Directories import SCOPE_CURRENT_SKIN, resolveFilename
from enigma import RT_HALIGN_LEFT, eListboxPythonMultiContent, gFont
from Tools.LoadPixmap import LoadPixmap
from skin import applySkinFactor, fonts, parameters


def ChoiceEntryComponent(key=None, text=["--"]):
	res = [text]
	if text[0] == "--":
		x, y, w, h = parameters.get("ChoicelistDash", applySkinFactor(0, 0, 900, 25))
		res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT, "-" * 200))
	else:
		if key:
			x, y, w, h = parameters.get("ChoicelistName", applySkinFactor(45, 0, 900, 25))
			res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT, text[0]))
			if key == "dummy":
				png = None
			elif key == "expandable":
				png = LoadPixmap(resolveFilename(SCOPE_CURRENT_SKIN, "icons/expandable.png"))
			elif key == "expanded":
				png = LoadPixmap(resolveFilename(SCOPE_CURRENT_SKIN, "icons/expanded.png"))
			elif key == "verticalline":
				png = LoadPixmap(resolveFilename(SCOPE_CURRENT_SKIN, "icons/verticalline.png"))
			elif key == "bullet":
				png = LoadPixmap(resolveFilename(SCOPE_CURRENT_SKIN, "icons/bullet.png"))
			else:
				png = LoadPixmap(resolveFilename(SCOPE_CURRENT_SKIN, "buttons/key_%s.png" % key))
			if png:
				x, y, w, h = parameters.get("ChoicelistIcon", applySkinFactor(5, 0, 35, 25))
				res.append((eListboxPythonMultiContent.TYPE_PIXMAP_ALPHABLEND, x, y, w, h, png))
		else:
			x, y, w, h = parameters.get("ChoicelistNameSingle", applySkinFactor(5, 0, 900, 40))
			res.append((eListboxPythonMultiContent.TYPE_TEXT, x, y, w, h, 0, RT_HALIGN_LEFT, text[0]))
	return res


class ChoiceList(MenuList):
	def __init__(self, list, selection=0, enableWrapAround=False):
		MenuList.__init__(self, list, enableWrapAround, eListboxPythonMultiContent)
		font = fonts.get("ChoiceList", applySkinFactor("Regular", 20, 30))
		self.l.setFont(0, gFont(font[0], font[1]))
		self.l.setItemHeight(font[2])
		self.selection = selection

	def postWidgetCreate(self, instance):
		MenuList.postWidgetCreate(self, instance)
		self.moveToIndex(self.selection)
		self.instance.setWrapAround(True)
