from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)



@hops.component(
    "/createGraphBM",
    name = "Create Graph Bruno",
    inputs=[
        hs.HopsInteger("X", "X", "Nodes in X", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Y", "Y", "Nodes in Y", hs.HopsParamAccess.ITEM, default= 1),
        hs.HopsInteger("Layout", "L", "Layout template", hs.HopsParamAccess.ITEM, default= 0),
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)
    ]
)
def createGraph(X, Y, layout):

    G = geo.createGridGraph(X, Y)
    GW = geo.addRandomWeigrhs(G)

    nodes = geo.getNodes(GW, layout)
    edges = geo.getEdges(GW, layout) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)