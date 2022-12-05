import sys 
import numpy as np

class PDB:
    def __init__(self):
        self.ATOM = []
        self.atomids = []
        self.alts = []
        self.names = []
        self.resns =[]
        self.chainids = []
        self.resids = []
        self.xs, self.ys, self.zs = [], [], []
        self.occupancy = []
        self.bfactors = []
        self.segids = []
        self.elem_symbols = []
        self.charges = []

    def read(self, pdb):
        with open(pdb, "r") as fin:
            for line in fin: 
                #print(line)
                if line[0:3].strip() == "TER" or line[0:3].strip() == "END":
                    self.ATOM.append(line[0:3])
                    continue
                self.ATOM.append(line[0:6])
                self.atomids.append(line[6:11])
                self.names.append(line[12:16])
                self.alts.append(line[16])
                self.resns.append(line[17:20])
                self.chainids.append(line[21])
                self.resids.append(line[22:26])
                self.xs.append(line[30:38])
                self.ys.append(line[38:46])
                self.zs.append(line[46:54])
                self.occupancy.append(line[54:60])
                self.bfactors.append(line[60:66])
                self.segids.append(line[73:76])
                self.elem_symbols.append(line[76:78])
                self.charges.append(line[78:90])
    
        return self

    def write(self, filename):
        # NOTE: END and TER lines are not written.
        with open(filename, "w") as fout:
            natoms = len(self.names)
            for i in range(natoms):
                line = self.ATOM[i]+self.atomids[i]+" "+self.names[i]+self.alts[i]\
                       +self.resns[i]+" "+self.chainids[i]+self.resids[i]+"    "\
                       +self.xs[i]+self.ys[i]+self.zs[i]\
                       +self.occupancy[i]+self.bfactors[i]+"       "+self.segids[i]+self.elem_symbols[i]+self.charges[i]
            
                fout.write(line)
        return None

    def get_crds(self):
        rs = []
        for x, y, z in zip(self.xs, self.ys, self.zs):
            x, y, z = float(x.strip()), float(y.strip()), float(z.strip())
            rs.append([x, y, z])

        return np.array(rs)

    def select_atoms(self, selection):
        ## Based on PyMOL selection
        # TODO:
        # I want to realise the following selection criteria:
        #     i.  name CA 
        #     ii. chain E and resname HIS and name CA
        #     iii. polymer within 6 of selection
        pass

def main():
    ## Usage:
    pdb = sys.argv[1] # A PDB file is given

    obj = PDB().read(pdb) # It is read

    rs = obj.get_crds() # Get all the coordinates typed ndarray

main()
