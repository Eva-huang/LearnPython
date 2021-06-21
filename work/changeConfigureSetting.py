import os

path = r"D:\Fullarch"
debugFile = []


def changeConfigureSetting(value):
    for r, d, f in os.walk(path):
        for file in f:
            if file.startswith('DebugParams.txt'):
                debugFile.append(os.path.join(r, file))
    for filepath in debugFile:
        lines = open(filepath).read().splitlines()
        for i, line in enumerate(lines):
            if 'FeatureOverlapThread' in line:
                lines[i] = 'FeatureOverlapThrshold: ' + value
                open(filepath, 'w').write('\n'.join(lines))


changeConfigureSetting('0.0')
