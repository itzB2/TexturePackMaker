from ctm.full import Full
from ctm.Constants import *
import argparse

parser = argparse.ArgumentParser(description='HAHA FULL CTM go BRRRRR')

parser.add_argument("image", type=str, help="The path to the normal texture")
parser.add_argument("imageWithNoSides", type=str, help="The path to the normal texture with no Sides")
parser.add_argument("SavePath", type=str, help="Where to save the files? idk")
parser.add_argument("OldBlockID", type=str, help="The block ID in case if u use the old one for pvp that's totally normal but using the newer version for pvp that's super weird")
parser.add_argument("NewBlockID", type=str, help="The new Block ID")
parser.add_argument("Metadata", type=int, help="The Metadata(Minecraft DataValue) of the block if u want to make it so it works for different colors")

args = parser.parse_args()

POG = Full(args.image, args.SavePath, args.imageWithNoSides, args.OldBlockID, args.NewBlockID, args.Metadata)
POG.run()