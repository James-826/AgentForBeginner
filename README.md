这是一个Agent学习项目，我将从0开始纯手打进行古法开发，来帮我更深入的学习Agent的知识。
我们首先开发基础功能的agent，但是会后续通过学习不同的内容来完善他的功能。

技术栈：
前端：
后端：python，FastApi，LangChain/OpeanAI SDK，Pydantic

项目架构：配置层+data层+session层+agentloop层+prompt层等

首先要有配置层，config里面配置我们的llm的api还有base_url，然后agent支持多种格式的llm，然后我们可以根据不同的比如cc或者openai来动态配置吧。

data层就是比如我们定义的工具的函数，还有工具的注册表，还有最重要的data通过pydantic来约束定义我们的比如result实体还有输入的接收的model。

session层就是可以帮我自动保存上下文，然后下次打开的时候可以自动吧上下文在渲染出来。

agentloop层为了方便学习，我们要手写循环本身，我想写一个workflow通过用户选择自动选plan还是react这两种。然后上下文的维护也要写到里面，还有权限控制，但是我感觉这样代码会很难维护，我在考虑要不要用graph的概念来实现循环的一个节点化。

然后就是prompt，我们定义静态和动态提示词，静态的有系统提示词比如目标是什么，角色定义，还有要怎么处理问题，最后还有约束。大概这样吧。

快速开始指南：（待开发）