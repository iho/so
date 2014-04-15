start:
	guake -n what
	guake -e "workon so && run"
	guake -s 0 
	guake -n what
	guake -e "workon so"
	guake -s 1
	guake -n what
	guake -e "workon so"
	guake -s 2
