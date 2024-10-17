
--- 
title:  基于JAVA的拼图小游戏源码，JAVA拼图小游戏设计与实现含详细文档 
tags: []
categories: [] 

---
## Java小游戏

### 一、设计思路

#### 1、分块

​ 首先将一张大图分为9块小图片，而后将小图片封装在一个类（继承JButton）因此每张图片都为一个按扭

```
public class Cell extends JButton {<!-- -->

    private static final long serialVersionUID = 8290188097137862984L;
    public static final int IMAGEWIDTH = 200; // 图片宽度
    private int place;// 图片位置

    public Cell(ImageIcon icon, int place) {<!-- -->
        this.setIcon(icon); // 单元图片的图标
        this.setSize(IMAGEWIDTH, IMAGEWIDTH);// 单元图片的大小
        this.place = place; // 单元图片的位置
    }

    public void setStateIcon(ImageIcon icon){<!-- -->
        this.setIcon(icon);
    }

    /*
     * 移动单元图片的方法
     */
    public void move(Direction dir) {<!-- -->
        Rectangle rec = this.getBounds();
        switch (dir) {<!-- -->
            case UP:
                this.setLocation(rec.x, rec.y - IMAGEWIDTH);
                break;
            case DOWN:
                this.setLocation(rec.x, rec.y + IMAGEWIDTH);
                break;
            case LEFT:
                this.setLocation(rec.x - IMAGEWIDTH, rec.y);
                break;
            case RIGHT:
                this.setLocation(rec.x + IMAGEWIDTH, rec.y);
                break;
        }
    }

    @Override
    public int getX() {<!-- -->
        return this.getBounds().x;
    }

    @Override
    public int getY() {<!-- -->
        return this.getBounds().y;
    }

    public int getPlace() {<!-- -->
        return place;
    }
}

```

#### 2、组合

​ 在创建一个Panel面板，以数组的方式将9个图片按钮类组合，并依次添加。

```
public void init() {<!-- -->
    int num = 0, c = 0;
    ImageIcon icon = null;
    Cell cell = null;
    for (int i = 0; i &lt; 3; i++) {<!-- -->
        for (int j = 0; j &lt; 3; j++) {<!-- -->
            num = i * 3 + j;
            icon = new ImageIcon(GamePanel.class.getResource((num) + ".jpg"));
            cell = new Cell(icon, num);// 实例化图片
            cell.setLocation(j * Cell.IMAGEWIDTH, i * Cell.IMAGEWIDTH);// 设置单元图片的坐标
            cells[c++] = cell;// 将单元图片储存到单元图片数组中
        }
    }
    for (int i = 0; i &lt; cells.length; i++) {<!-- -->
        this.add(cells[i]);
    }
    this.add(Start);
}

```

此时面板上面显示的是最初完整的状态，我们需要将它们打乱

<img src="https://img-blog.csdnimg.cn/img_convert/2f216ce6c12612c151b0f04d83dc094a.png" alt="image-20210320135518089">

#### 3、打乱

​ 这里用到的打乱算法比较简单，就是模拟用户随机移动，在大量的移动之下模块自然打乱

```
public void random(){<!-- -->
    Random random = new Random();
    int m, count = 0;
    while (count &lt; 500) {<!-- -->
        m = random.nextInt(9);
        swap(cells[m]);//移动算法
        count++;
    }
    Start.setSelected(false);
}

```

移动算法如下：

```
public void swap(Cell cell) {<!-- -->
    int x = cellBlank.getX();
    int y = cellBlank.getY();
    if ((x - cell.getX()) == Cell.IMAGEWIDTH &amp;&amp; cell.getY() == y) {<!-- -->
        cell.move(Direction.RIGHT);
        cellBlank.move(Direction.LEFT);
    } else if ((x - cell.getX()) == -Cell.IMAGEWIDTH &amp;&amp; cell.getY() == y) {<!-- -->
        cell.move(Direction.LEFT);
        cellBlank.move(Direction.RIGHT);
    } else if (cell.getX() == x &amp;&amp; (cell.getY() - y) == Cell.IMAGEWIDTH) {<!-- -->
        cell.move(Direction.UP);
        cellBlank.move(Direction.DOWN);
    } else if (cell.getX() == x &amp;&amp; (cell.getY() - y) == -Cell.IMAGEWIDTH) {<!-- -->
        cell.move(Direction.DOWN);
        cellBlank.move(Direction.UP);
    }
}

```

​ 首先我们需要判断交换对象是位于空白对象的何处，这样才好移动它们两个（空白图片和待移动图片）。

​ 此时图片已经打乱

<img src="https://img-blog.csdnimg.cn/8ff6177206a447f790d6808c12075ffc.png" alt="在这里插入图片描述">

#### 4、成功与否

​ 此时图片待玩家拼成功，这需要我们在图片按钮每次按下的监听事件中添加判断成功与否。

```
public boolean isSuccess() {<!-- -->
    for (int i = 0; i &lt; cells.length; i++) {<!-- -->
        int x = cells[i].getX();
        int y = cells[i].getY();
        if (i != 0) {<!-- -->
            if ((y / Cell.IMAGEWIDTH * 3 + x / Cell.IMAGEWIDTH) != cells[i].getPlace()) {<!-- -->
                return false;
            }
        }
    }
    return true;
}

```

​ 我们需要判断每张图片是否是在原来位置上，若全部图片都在原位上，则是成功！

​ 鼠标监听事件如下：

```
@Override
public void mousePressed(MouseEvent e) {<!-- -->
    // TODO Auto-generated method stub
    Cell cell = (Cell) e.getSource();// 获取触发时间的对象
    swap(cell);
    if (isSuccess()) {<!-- -->
        cellBlank.setStateIcon(new ImageIcon(GamePanel.class.getResource("1010.jpg")));//将空白图片变为完整的图片
        this.repaint();
        int i = JOptionPane.showConfirmDialog(this, "成功！再来一局？？", "拼图成功", JOptionPane.YES_NO_OPTION);
        if (i == JOptionPane.YES_OPTION) {<!-- -->
            cellBlank.setStateIcon(new ImageIcon(GamePanel.class.getResource("8.jpg")));
            Start.setSelected(true);
            random();
        }else if (i == JOptionPane.NO_OPTION) {<!-- -->
            System.exit(0);
        }
    }
}

```

### 二、游戏测试

<img src="https://img-blog.csdnimg.cn/img_convert/7bf290d68c337e4461d2654b383c00fa.png" alt="image-20210320140431638"> 完整代码下载地址：
