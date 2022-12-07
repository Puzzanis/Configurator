STYLESHEET = '''QTreeWidget {border:none;} 

        QTreeView::branch:has-siblings:adjoins-item {
            border-image: url(icon/branch-more.png) 0;}

        QTreeView::branch:has-siblings:!adjoins-item {
            border-image: url(icon/vline.png) 0;}

        QTreeView::branch:has-children:!has-siblings:closed,
        QTreeView::branch:closed:has-children:has-siblings {
            border-image: none;
            image: url(icon/branch-closed.png);}

        QTreeView::branch:open:has-children:!has-siblings,
        QTreeView::branch:open:has-children:has-siblings {
            border-image: none;
            image: url(icon/branch-open.png);}

        QTreeView::branch:!has-children:!has-siblings:adjoins-item {
            border-image: url(icon/branch-end.png) 0;}'''