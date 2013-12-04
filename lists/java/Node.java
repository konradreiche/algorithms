/**
 * @author Konrad Reiche
 *
 */
public class Node<T> {

    private Node<T> next;
    private T data;

    public Node(T value) {
        this.data = value;
    }

    public Node<T> next() {
        return this.next;
    }

    public T value() {
        return this.data;
    }

    public void setNext(Node<T> next) {
        this.next = next;
    }

    public void setData(T data) {
        this.data = data;
    }

}
