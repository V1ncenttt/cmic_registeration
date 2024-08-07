from sys import platform
import os


class Operator:
    def __init__(self, *args, **kwargs):
        self.niftyreg_dir = "../niftk-18.5.4/bin"

    def multiply(self, img1, img2, output_name=None):
        mul_command = self.niftyreg_dir + "reg_tools -in " + img1 + " -mul " + img2
        if output_name:
            nan_command += " -out " + output_name

        os.system(mul_command)

    def add(self, img1, img2, output_name=None):
        add_command = self.niftyreg_dir + "reg_tools -in " + img1 + " -add " + img2
        if output_name:
            nan_command += " -out " + output_name

        os.system(add_command)

    def substract(self, img1, img2, output_name=None):
        substract_command = (
            self.niftyreg_dir + "reg_tools -in " + img1 + " -sub " + img2
        )
        if output_name:
            nan_command += " -out " + output_name

        os.system(substract_command)

    def divide(self, img1, img2, output_name=None):
        divide_command = self.niftyreg_dir + "reg_tools -in " + img1 + " -div " + img2
        if output_name:
            nan_command += " -out " + output_name

        os.system(divide_command)

    def nan(self, img, mask, output_name=None):
        nan_command = self.niftyreg_dir + "reg_tools -in " + img + " -nan " + mask
        if output_name:
            nan_command += " -out " + output_name

        os.system(nan_command)
