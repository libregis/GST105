import os

docs = "docs"
figures = docs + "/figures"
data = "data"

if not os.path.exists(docs):
    os.mkdir(docs)

if not os.path.exists(figures):
    os.mkdir(figures)

if not os.path.exists(data):
    os.mkdir(data)


qgis = "QGIS 2.4 and GRASS 6.4.4"

for lab in range(0,9):
    os.system("git mv '{0}' '{1}'".format("Module {0} Lab/{1}/Module {0} Lab.md".format(lab, qgis), "{0}/Lab{1}.md".format(docs, lab)))
    os.system("git mv '{0}' '{1}'".format("Module {0} Lab/{1}/figures".format(lab, qgis), "{0}/Lab{1}".format(figures, lab)))
    os.system("git mv '{0}' '{1}'".format("Module {0} Lab/{1}/Lab {0} Data".format(lab, qgis), "{0}/Lab{1}".format(data, lab)))
    os.system("git mv '{0}' '{1}'".format("Module {0} Lab/{1}/Lab {0} Data.zip".format(lab, qgis),
                                          "{0}/Lab{1}".format(data, lab)))

    os.system("git rm -rf '{0}'".format("Module {0} Lab/".format(lab)))
