import xml.etree.ElementTree as ET
import re
from tree import Tree
from node import Node
from constraint import Constraint
from flag import Flag
from constraintrepo import ConstraintRepo

class XmlParser(object):
  patFeature = ':(\S?)\s+([\w-]*)\((\w+)\)\s*\[?\d?,?(.?)\]?'

  def getConstraintText(self, constraint):
    match = re.search(':([\w\W]*)', constraint)
    return match.group(1)

  def parseFeatureTree(self, xmlFile):
    tree = Tree()
    xmlTree = ET.parse(xmlFile)
    xmlRoot = xmlTree.getroot()
    features = xmlRoot.find('feature_tree').text.split('\n')
    for feature in features:
      if not feature or feature.isspace(): continue
      match = re.search(XmlParser.patFeature, feature)
      type = match.group(1) + match.group(4)
      name = match.group(2)
      id = match.group(3)
      node = Node(id, name, type)
      tree.addNode(node)
    return tree

  def parseConstraints(self, xmlFile):
    constraintrepo = ConstraintRepo()
    xmlTree = ET.parse(xmlFile)
    xmlRoot = xmlTree.getroot()
    constraints = xmlRoot.find('constraints').text.split('\n')
    for constraint in constraints:
      if not constraint or constraint.isspace(): continue
      constraintText = self.getConstraintText(constraint)
      constraintrepo.addConstraint(self.createConstraint(constraintText))
    return constraintrepo


  def createConstraint(self, constraintText):
    constraint = Constraint()
    flags = [x.strip() for x in constraintText.split("or")]
    for item in flags:
      if item[0] == '~':
        flag = Flag(item[1:], True)
        constraint.addFlag(flag)
      else:
        flag = Flag(item, False)
        constraint.addFlag(flag)
    return constraint
