public class Stack
{
	private int data;
	public Stack* next;

	public Stack(int val)
	{
		data = val;
		next = NULL;
	}
	public void push(int val)
	{
		Stack newNode = new Stack(val);
		newNode.next = this.next;
		this.next = newNode;
	}
	public int pop()
	{
		result = data;
		this.next = this.next.next;
		return result;
	}
	public int peek()
	{
		return data;
	}
	public boolean isEmpty()
	{
		return next == NULL;
	}
	public void print()
	{
		System.out.println(data);
		if(this.next != NULL)
			this.next.print();
	}

	public static void main(String args[])
	{
		Stack stack = new Stack(1);
		stack.push(2);
		System.out.println("First:");
		stack.print();
		System.out.println("Second:");
		stack.push(3);
		stack.print();
		System.out.println(stack.pop());
		System.out.println(stack.peek());
	}
}
