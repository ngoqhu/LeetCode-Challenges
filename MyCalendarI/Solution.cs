public class ListNode {
	public int Start { get; set; }
	public int End { get; set; }
	public ListNode Next { get; set; }
		
	public ListNode(int start, int end, ListNode next)	{
		Start = start;
		End = end;
		Next = next;
	}
}

public class MyCalendar {
    public ListNode Head { get; set; }
    
    public MyCalendar() {
        ListNode tail = new ListNode(Int32.MaxValue, Int32.MaxValue, null);
		Head = new ListNode(-1, -1, tail);
    }
    
    public bool Book(int start, int end) {
        ListNode current = Head;
		ListNode last = Head;
			
		while (current.Start < start)	{
			last = current;
			current = current.Next;
		}
			
		if (last.End > start || current.Start < end)	{
			return false;
		}
			
		last.Next = new ListNode(start, end, current);
		return true;
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * bool param_1 = obj.Book(start,end);
 */
