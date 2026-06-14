import NaiveRAG as rag
from fastapi import FastAPI
from pydantic import BaseModel,Field

class rag_request(BaseModel):
    input:str=Field(...,decription="输入文本")
class rag_response(BaseModel):
    result:str=Field(...,decription="输出文本")
    status:str
app=FastAPI()

@app.post("/rag",response_model=rag_response)
def rag_endpoint(request:rag_request):
    result=rag.chain.invoke({"input":request.input})
    return rag_response(result=result,status="success")