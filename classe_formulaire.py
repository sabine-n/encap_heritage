#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:14:46 2020

@author: utilisateur
"""

class formulaire:
    def __init__(self, nom, prenom, naissance):
        self.nom = nom.upper()
        self.prenom = prenom
        self.naissance = naissance
        
    def _set_naissance(self, naissance):
        if isinstance(naissance, list):
            na = ''.join([str(x) for x in naissance])
            if na.isnumeric():
                self._naissance = int(na)
            else:
              self._naissance = 1900  
        else:
            na = str(naissance)
        if na.isnumeric():
            self._naissance = int(na)
        else:
            self._naissance = 1900
            
    def _get_naissance(self):
        print("Valeur de Naissance :" , self._naissance)
        return  self._naissance
    naissance = property(_get_naissance, _set_naissance)
    
    def _set_nom(self, nom):
        self._nom = str(nom).upper()
    def _set_prenom(self, prenom):    
        self._prenom = str(prenom).upper()
    def _get_nom(self):
        return self._nom
    def _get_prenom(self): 
        return self._prenom
    nom = property(_get_nom, _set_nom)
    prenom = property(_get_prenom, _set_prenom)
    def age(self):
        return 2020 - self._naissance
    def majeur(self):
        return self.age() >= 18
    def memeFamille(self, formulaire):
        return self.nom == formulaire.nom
    def memePersonne(self, formulaire):
        return self.nom == formulaire.nom and self.prenom == formulaire.prenom and self.anneeNaissance == formulaire.anneeNaissance
    def __str__(self): # def __repr__(self):
        return '('+self.nom+', '+self.prenom+', %s)' % (self.naissance)
 
    

class data(formulaire):
    def __init__(self, nom, prenom, naissance):
        formulaire.__init__(self, nom, prenom, naissance)
    def buildID(self):
        self.id = self.nom[:2]
        self.id += self.prenom[:2]
        self.id += str(self.age())

    
class recensement:
    def __init__(self, l1, l2, l3):
        self.f2020 = l3
        self.f2019 = l2
        self.f2018 = l1
        
    def permanents(self):
        return [f for f in self.f2020 if
               f in self.f2019 and f in self.f2018]
    
class listeelectorale(recensement):
    def __init__(self, l1, l2, l3):
        recensement.__init__(self, l1, l2, l3)
        
    def inscrits(self):
        return [f for f in self.permanents() if
                f.majeur()]

jd = formulaire('Doe', 'John', 2005)
ad = formulaire('Doe', 'Alice', 2000)
sn = formulaire('Nasr', 'Sabine', 1992)
kb = formulaire('Bryant', 'Kobe', 1978)
so = formulaire("O'neal", 'Shaquille', 1972)
ld = formulaire('David', 'Larry', 1947)
jh = formulaire('Hendrix', 'Jimi', 1942)


l = listeelectorale([jd, ad, sn], [kb, so, ld, jh], [ad, sn, so])

for f in l.inscrits():
    print(f)

jd = data('Doe', 'John', 2005)
jd.buildID()

jh = data('Hendrix', 'Jimi', 1942)
jh.buildID()
#print(jd.majeur())
#print(ad.majeur())
#print(jd.memeFamille(ad))
#print(jd, ad)
#rint(ad)

liste_formulaire=[]
liste_formulaire.append(jd)
liste_formulaire.append(ad)
liste_formulaire.append(sn)
liste_formulaire.append(kb)
liste_formulaire.append(so)
liste_formulaire.append(ld)
liste_formulaire.append(jh)


a = sorted(liste_formulaire, key = lambda year : year.naissance)

for i in a:
    print(i)
    

#print(sorted(liste_formulaire, key = lambda year : year.anneeNaissance))


