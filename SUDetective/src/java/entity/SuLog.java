/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package entity;

import java.io.Serializable;
import javax.persistence.*;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import javax.xml.bind.annotation.XmlRootElement;

/**
 *
 * @author mbaty001
 */
@Entity
@Table(name = "SU_LOG")
@XmlRootElement
@NamedQueries({
    @NamedQuery(name = "SuLog.findAll", query = "SELECT s FROM SuLog s"),
    @NamedQuery(name = "SuLog.findByIdSULOG", query = "SELECT s FROM SuLog s WHERE s.idSULOG = :idSULOG"),
    @NamedQuery(name = "SuLog.findByLogFile", query = "SELECT s FROM SuLog s WHERE s.logFile = :logFile"),
    @NamedQuery(name = "SuLog.findByNodeName", query = "SELECT s FROM SuLog s WHERE s.nodeName = :nodeName")})
public class SuLog implements Serializable {
    @Basic(optional = false)
    @NotNull
    @Column(name = "LOG_ERRORS")
    private int logErrors;
    private static final long serialVersionUID = 1L;
    @Id
    @Basic(optional = false)
    @NotNull
    @Column(name = "idSU_LOG")
    private Integer idSULOG;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "LOG_FILE")
    private String logFile;
    @Basic(optional = false)
    @NotNull
    @Size(min = 1, max = 2000000000)
    @Column(name = "NODE_NAME")
    private String nodeName;
    @JoinColumn(name = "SU_idSU", referencedColumnName = "idSU")
    @ManyToOne(optional = false)
    private Su sUidSU;
    @JoinColumn(name = "NODE_TYPE_idNODE_TYPE", referencedColumnName = "idNODE_TYPE")
    @ManyToOne(optional = false)
    private NodeType nODETYPEidNODETYPE;
    @JoinColumn(name = "HW_TYPE_idHW_TYPE", referencedColumnName = "idHW_TYPE")
    @ManyToOne(optional = false)
    private HwType hWTYPEidHWTYPE;

    public SuLog() {
    }

    public SuLog(Integer idSULOG) {
        this.idSULOG = idSULOG;
    }

    public SuLog(Integer idSULOG, String logFile, String nodeName) {
        this.idSULOG = idSULOG;
        this.logFile = logFile;
        this.nodeName = nodeName;
    }

    public Integer getIdSULOG() {
        return idSULOG;
    }

    public void setIdSULOG(Integer idSULOG) {
        this.idSULOG = idSULOG;
    }

    public String getLogFile() {
        return logFile;
    }

    public void setLogFile(String logFile) {
        this.logFile = logFile;
    }

    public String getNodeName() {
        return nodeName;
    }

    public void setNodeName(String nodeName) {
        this.nodeName = nodeName;
    }

    public Su getSUidSU() {
        return sUidSU;
    }

    public void setSUidSU(Su sUidSU) {
        this.sUidSU = sUidSU;
    }

    public NodeType getNODETYPEidNODETYPE() {
        return nODETYPEidNODETYPE;
    }

    public void setNODETYPEidNODETYPE(NodeType nODETYPEidNODETYPE) {
        this.nODETYPEidNODETYPE = nODETYPEidNODETYPE;
    }

    public HwType getHWTYPEidHWTYPE() {
        return hWTYPEidHWTYPE;
    }

    public void setHWTYPEidHWTYPE(HwType hWTYPEidHWTYPE) {
        this.hWTYPEidHWTYPE = hWTYPEidHWTYPE;
    }

    @Override
    public int hashCode() {
        int hash = 0;
        hash += (idSULOG != null ? idSULOG.hashCode() : 0);
        return hash;
    }

    @Override
    public boolean equals(Object object) {
        // TODO: Warning - this method won't work in the case the id fields are not set
        if (!(object instanceof SuLog)) {
            return false;
        }
        SuLog other = (SuLog) object;
        if ((this.idSULOG == null && other.idSULOG != null) || (this.idSULOG != null && !this.idSULOG.equals(other.idSULOG))) {
            return false;
        }
        return true;
    }

    @Override
    public String toString() {
        return "entity.SuLog[ idSULOG=" + idSULOG + " ]";
    }

    public int getLogErrors() {
        return logErrors;
    }

    public void setLogErrors(int logErrors) {
        this.logErrors = logErrors;
    }
    
}
