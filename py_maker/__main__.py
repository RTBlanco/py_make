from py_maker.author import Author
import sys
# from py_maker.make_package.package import package 
# from py_maker.config.json_writer import update_config
from py_maker.projects import Package


def main():
  user = Author.new()


  param1 = sys.argv[1]

  if len(sys.argv) >= 3:
    project_name_input = sys.argv[2] 
    version_input = sys.argv[3] if len(sys.argv) == 4 else None

  if param1 == "init":
    user.update()
  else:
    pkg = Package.new(project_name_input,version_input)
    test = input("Create with test folder ?(y/n)")
    
    while True:
      if test.lower() == "y" and len(test.lower()) == 1:
        pkg.make(True)
      elif test.lower() == "n" and len(test.lower()) == 1:
        pkg.make()
      else:
        print("only (y) or (n)\n")
  

    
      

if __name__=="__main__":
  main()