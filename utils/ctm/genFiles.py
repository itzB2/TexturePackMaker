import os

def genProps(sides, name, p_id, path, tiles, method, metadata, save):

	string = ""
	try:
		f = open(os.path.join(path, name)+".properties", "x")
	except:
		f = open(os.path.join(path, name)+".properties", "w")
	f.write(f"method={method}\n")
	string += f"method={method}\n" if save else ""
	f.write(f"tiles=0-{str(tiles)}\n")
	string += f"tiles=0-{str(tiles)}\n" if save else ""
	if sides != "":
		f.write(f"sides={sides}\n")
		string += f"sides={sides}\n" if save else ""
	else:
		pass
	f.write(f"matchBlocks={p_id}\n")
	string += f"matchBlocks={p_id}\n" if save else ""
	if sides != 0:
		f.write(f"metadata={metadata}")
		string += f"metadata={metadata}" if save else ""
	else:
		pass
	if save:
		f.close()
	else:
		return string

def AnimationMcMeta(frameTime, fPath):
	f = open(fPath, "w")
	tabRes = ""
	content = "{"
	tabRes += "\t"
	content += tabRes
	content += f"\"animation\":"
	tabRes += "\t"
	content += tabRes + f"\"frametime\":{frameTime}" if frametime != 0 else ""
	content += "}"
	content += "}"

	f.write(content)
	f.close()