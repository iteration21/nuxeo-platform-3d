import bpy, json, os, sys, time, bmesh
from bpy import context
from bpy_extras.object_utils import world_to_camera_view
from copy import copy
from math import pi, cos, sin, degrees, radians
from mathutils import Vector
import argparse


def sphericalCoords(s):
    try:
        if s == '':
            return 0, 0
        zenith, azimuth = map(int, s.split(','))
        return zenith, azimuth
    except:
        raise argparse.ArgumentTypeError('Coordinates must be zenith,azimuth')


def dimensions(d):
    try:
        if d == '':
            return 0, 0
        width, height = map(int, d.split(','))
        return width, height
    except:
        raise argparse.ArgumenTypeError('Dimensions must be width,height')


parser = argparse.ArgumentParser(description='Blender pipeline.')
parser.add_argument('-i', '--input', dest='input',
                    help='path for the input file')
parser.add_argument('-o', '--outdir', dest='outdir',
                    help='path for output dir')
parser.add_argument('-op', '--operators', dest='operators', nargs='*', choices=['import', 'lod', 'render', 'convert'],
                    help='a list of operators to run in the pipeline (options: import,lod,render,convert)')
parser.add_argument('-li', '--lodids', dest='lodids', nargs='*',
                    help='a list of ids to use on lod')
parser.add_argument('-l', '--lods', dest='lods', nargs='*',
                    help='a list of level of detail values to use on the lod operator (options: 0-100)')
parser.add_argument('-mp', '--maxpolys', dest='maxpolys', nargs='*',
                    help='a list of max polygon values to use on the lod operator')
parser.add_argument('-ri', '--renderids', dest='renderids', nargs='*',
                    help='a list of ids to use on render')
parser.add_argument('-d', '--dimensions', help='list of dimensions for render',
                    dest='dimensions', type=dimensions, nargs='*')
parser.add_argument('-c', '--coords', help='list of spherical coordinates for render',
                    dest='coords', type=sphericalCoords, nargs='*')

args_to_parse = sys.argv[sys.argv.index('--') + 1:]
print(args_to_parse)
args = parser.parse_args(args_to_parse)
print('operators:')
print(args)
if args.operators is None:
    sys.exit()

base_path = os.path.dirname(os.path.abspath(__file__)) + '/pipeline/'
lod = current_lod = calculated_lod = 100
lodid = 'original'
max_polygons = 9999

# turn all elements of the lods list into integers
if args.lods is not None and args.lods[0] != '':
    args.lods = [int(lod) for lod in args.lods]

for operator in args.operators:
    if operator == 'lod':
        lodid = args.lodids.pop(0)
        # get the biggest lod value from the lods list
        lodindex = args.lods.index(max(args.lods))
        current_lod = int(args.lods.pop(lodindex))
        calculated_lod = int((current_lod / lod) * 100)
        lod = current_lod
        max_polygons = args.maxpolys.pop(lodindex)
    if operator == 'render':
        coords = args.coords.pop(0)
        dim = args.dimensions.pop(0)
        id = args.renderids.pop(0)
    filename = base_path + operator + '.py'
    exec (compile(open(filename).read(), filename, 'exec'))
