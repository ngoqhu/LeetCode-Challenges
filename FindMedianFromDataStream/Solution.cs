public class MedianFinder
{
    private int _left = -1;
    private int _right;
    private bool _flag;
    private readonly List<int> _numbers;

    public MedianFinder()
    {
        _numbers = new List<int>();
    }

    public void AddNum(int num)
    {
        var index = _numbers.BinarySearch(num);
        index = index >= 0 ? index : ~index;
        _numbers.Insert(index, num);
        if (_flag)
        {
            _right++;
        }
        else
        {
            _left++;
        }

        _flag = !_flag;
    }

    public double FindMedian()
    {
        return (_numbers[_left] + _numbers[_right]) / 2D;
    }
}
/*
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */
