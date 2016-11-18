from xmlparser import XmlParser

parser = XmlParser()
tree = parser.parseFeatureTree('data//linux.xml')
tree.visualize()

constraintrepo = parser.parseConstraints('data//linux.xml')
#print constraintrepo.getNumOfConstraintsViolated()
