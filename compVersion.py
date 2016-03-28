def compareVersion(self, v1, v2):
   _v1 = [int(v) for v in v1.split(".")]
   _v2 = [int(v) for v in v2.split(".")]
   for i in range(max(len(v1), len(v2))):
      version1 = _v1[i] if i < len(_v1) else 0
      version2 = _v2[i] if i < len(_v2) else 0
      if version1 > version2:
         return 1
      elif version1 < version2:
         return -1
   return 0
