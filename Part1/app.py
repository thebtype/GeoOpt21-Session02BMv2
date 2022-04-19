from tkinter import SOLID
import rhino3dm as rg
import networkx as nx
from flask import Flask
import ghhops_server as hs

app = Flask(__name__)
hops = hs.Hops(app)

@hops.component(
    "/movesolids",
    name = "Move Solid",
    inputs=[
        hs.HopsCurve("Curve", "Crv", "Shape of solid", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Y Axis", "Y", "Distance in Y", hs.HopsParamAccess.ITEM),
        hs.HopsInteger('X axis', 'X', 'Distance in X',hs.HopsParamAccess.ITEM, default=10),
        hs.HopsInteger('Number of boxes', 'Num_Int', 'Number of Solids',hs.HopsParamAccess.ITEM, default=10)
    ],
    outputs=[
       hs.HopsBrep("Solids", "Sol", "Moved Solids", hs.HopsParamAccess.LIST)
    ]
)

def movesolids(curve, Y, X, N):
    moved_solids=[]
    for i in range(N):
        vector =  rg.Vector3d(X*i/2,Y*i/2,0)
        sol=rg.Extrusion.Create(curve, 10, True)
        solCopy = sol.Duplicate()
        solCopy.Translate(vector)
        moved_solids.append(solCopy)
    return moved_solids

if __name__== "__main__":
    app.run(debug=True)