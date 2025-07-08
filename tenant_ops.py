#!/usr/bin/env python3

from aciapi import *
import sys
import argparse

ctrl=Reseau()

def main():
    parser = argparse.ArgumentParser(description="Script de gestion simple")
    
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--ajoute", metavar="VALEUR", help="Ajouter un tenant")
    group.add_argument("-d", "--delete", metavar="VALEUR", help="Supprime un tenant")
    group.add_argument("-l", "--list", metavar="VALEUR", help="Liste les tenants")
    
    args = parser.parse_args()

    if args.ajoute: ctrl.get_tenant(args.ajoute)
    if args.delete: ctrl.delete_tenant(args.delete)
    if args.list: print ("\n".join(ctrl.list_tenants()))


if __name__ == "__main__":
    if (not ctrl.get_session()): exit(0)

    main()


