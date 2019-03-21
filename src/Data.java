public class Data {
    private int currX;
    private int currY;
    private int targetX;
    private int targetY;

    public Data(int currX, int currY, int targetX, int targetY) {
        this.currX = currX;
        this.currY = currY;
        this.targetX = targetX;
        this.targetY = targetY;
    }

    public int getCurrX() {
        return currX;
    }

    public void setCurrX(int currX) {
        this.currX = currX;
    }

    public int getCurrY() {
        return currY;
    }

    public void setCurrY(int currY) {
        this.currY = currY;
    }

    public int getTargetX() {
        return targetX;
    }

    public void setTargetX(int targetX) {
        this.targetX = targetX;
    }

    public int getTargetY() {
        return targetY;
    }

    public void setTargetY(int targetY) {
        this.targetY = targetY;
    }

    public boolean cmp() {
        return (this.currX == this.targetX) && (this.currY == this.targetY);
    }

    @Override
    public String toString() {
        return "X: " + this.currX + " Y: " + this.currY + "\nTx: " + this.targetX + " Ty: " + this.targetY;
    }
}
