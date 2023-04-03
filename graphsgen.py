import matplotlib.pyplot as plt

def generate_graph(operation, result, num1, num2, root):
    if operation == 'addition':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('addition results')
        ax.set_xlabel('values')
        ax.set_ylabel('sum')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    if operation == 'subtraction':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('Subtraction results')
        ax.set_xlabel('values')
        ax.set_ylabel('sub')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
        
    if operation == 'multiplication':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('multiplication results')
        ax.set_xlabel('values')
        ax.set_ylabel('mult')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()

    if operation == 'division':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('division results')
        ax.set_xlabel('values')
        ax.set_ylabel('div')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()

    if operation == 'exponentiation':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('exponentiation results')
        ax.set_xlabel('values')
        ax.set_ylabel('pow')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    if operation == 'percentage':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('percentage results')
        ax.set_xlabel('values')
        ax.set_ylabel('per')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
        
    if operation == 'modulus':
        x = ['number 1', 'number 2', 'result']
        y = [num1, num2, result]
        fig, ax = plt.subplots(figsize=(5, 4))
        ax.bar(x, y)
        ax.set_title('modulo Results')
        ax.set_xlabel('values')
        ax.set_ylabel('mod')
        fig.canvas.manager.window.wm_geometry("+%d+%d" % (root.winfo_x() + root.winfo_width(), root.winfo_y()))
        plt.show()
    
    